<template>
  <div id="Categories">
    <div class="row">
      <div class="col-sm-12" style="padding: 20px">
        <div class="card">
          <div class="card-header">Gestión de categorias</div>
          <div class="card-body">
            <div class="row">
              <div class="col-sm-12 text-end">
                <button type="button" class="btn btn-success">Nueva</button>
              </div>
            </div>
            <div class="row">
              <div class="col-sm-12 table-responsive">
                <table class="table table-striped table-hover">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Nombre</th>
                      <th scope="col">Descripción</th>
                      <th class="text-center" scope="col">Opciones</th>
                    </tr>
                  </thead>
                  <tbody id="table-categorias-body">
                    <tr v-for="categoria in categorias">
                      <td>{{ categoria.id }}</td>
                      <td>{{ categoria.name }}</td>
                      <td>{{ categoria.description }}</td>
                      <td class="text-center" style="width: 20%">
                        <button
                          type="button"
                          class="btn btn-success"
                          v-on:click="getCategoria(categoria.id)"
                        >
                          Ver
                        </button>
                        <button type="button" class="btn btn-success">
                          Editar
                        </button>
                        <button type="button" class="btn btn-success">
                          Eliminar
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6">adfa</div>
    </div>
    <div id="modalVerCategoria" class="modal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Ver categoria</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="row">
                <div class="col-sm-6 text-end">
                  <strong>Id:</strong>
                </div>
                <div class="col-sm-6">
                  <label>{{categoria.id}}</label>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6 text-end">
                  <strong>Nombre:</strong>
                </div>
                <div class="col-sm-6">
                  <label>{{categoria.name}}</label>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6 text-end">
                  <strong>Descripción:</strong>
                </div>
                <div class="col-sm-6">
                  <label>{{categoria.description}}</label>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Cerrar
            </button>
          </div>
        </div>
      </div>
    </div>
    <h2>
      Usuario autenticado: <span>{{ username }}</span>
    </h2>
    <div>
      <h4>Registrar Categoría</h4>
      <input
        name="categoria_name"
        type="text "
        v-model="categoriaInput.name"
        placeholder="Nombre"
      />
      <input
        name="categoria_description"
        type="text"
        v-model="categoriaInput.description"
        placeholder="Descripción"
      />
      <button v-on:click="postCategory">Guardar</button>
      <br />
      <label>{{ mensaje }}</label>
      <br />
      <br />
    </div>
    <label for="CategoriaId">Categoria Id</label>
    <input
      name="CategoriaId"
      type="number"
      v-model="categoriaId"
      placeholder="Digite un Id Valido"
    />
    <button>Obtener categoría</button>
    <h2>
      La categoría con id = <span>{{ category_id }}</span
      >, tiene el nombre <span>{{ name }}</span> y su descripción es «<span>{{
        description
      }}</span
      >».
    </h2>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Categories",

  data: function () {
    return {
      categorias: [],
      categoria: {},
      category_id: "",
      name: "",
      description: "",
      categoriaId: 1,
      categoriaInput: {
        name: "",
        description: "",
      },
      mensaje: "",
    };
  },

  created: function () {
    this.username = this.$route.params.username;
    let self = this;
    this.getCategorias();
  },

  methods: {
    getCategorias: function () {
      let self = this;
      axios
        .get(`http://localhost:4000/categories/`)
        .then((result) => {
          self.categorias = result.data;
        })
        .catch((error) => {
          console.log(error);
          console.log(typeof error);
          alert("ERROR de Servidor");
        });
    },

    getCategoria: function (categoriaId) {
      this.username = this.$route.params.username;
      let self = this;

      axios
        .get(`http://localhost:4000/categories/${categoriaId}`)
        .then((result) => {
          self.categoria = result.data;
          self.abrirModalVerCategoria();
        })
        .catch((error) => {
          console.log(error);
          console.log(typeof error);
          alert("ERROR de Servidor");
        });
    },

    abrirModalVerCategoria() {
      let self = this;
      var modalVerCategoria = new bootstrap.Modal(
        document.getElementById("modalVerCategoria")
      );
      modalVerCategoria.show();
    },

    postCategory: function () {
      this.username = this.$route.params.username;
      let self = this;
      console.log(self.categoriaInput);
      axios
        .post(`http://localhost:4000/categories/`, self.categoriaInput)
        .then((result) => {
          console.log(result);
          self.mensaje = "Categoria Registrada Correctamente";
        })
        .catch((error) => {
          console.log(error);
          console.log(typeof error);
          alert("ERROR de Servidor");
        });
    },
  },
};
</script>

<style>
</style>
