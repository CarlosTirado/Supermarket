<template>
  <div id="Login" class="container">
    <div class="row">
      <div class="col-sm-12" style="padding: 20px">
        <div class="card">
          <div class="card-header text-bold">Iniciar Sesión</div>
          <div class="card-body">
            <div class="row">
              <div class="col-sm-12">
                <div class="mb-3">
                  <label for="usuario" class="form-label">Usuario</label>
                  <input type="text" class="form-control" v-model="username">
                </div>
                <div class="mb-3">
                  <label for="usuario" class="form-label">Contraseña</label>
                  <input type="password" class="form-control" v-model="password">
                </div>
				<div class="d-grid gap-2">
                	<button class="btn btn-primary" v-on:click='getUser'>Ingresar</button>
				</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

	<div id="modalRegistroUsuario" class="modal" tabindex="-1">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title">Registrar Usuario</h5>
					<button
						type="button"
						class="btn-close"
						data-bs-dismiss="modal"
						aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<div class="">
						<div class="row" style="margin-bottom: 10px">
							<div class="col-sm-6 text-end">
								<strong>Usuario:</strong>
							</div>
							<div class="col-sm-6">
								<input
								autocomplete="off"
								name="username"
								type="text"
								v-model="userInput.username"
								placeholder="Nombre"
								class="form-control"
								/>
							</div>
						</div>
						<div class="row">
							<div class="col-sm-6 text-end">
								<strong>Contraseña:</strong>
							</div>
							<div class="col-sm-6">
								<input
								autocomplete="off"
								name="password"
								type="password"
								v-model="userInput.password"
								placeholder="Descripción"
								class="form-control"
								/>
							</div>
						</div>
					</div>
				</div>
				<div class="modal-footer">
					<button
						type="button"
						class="btn btn-success"
						v-on:click="postUser"
						data-bs-dismiss="modal">
						Guardar
					</button>
					<button
						type="button"
						class="btn btn-secondary"
						data-bs-dismiss="modal">
						Cerrar
					</button>
				</div>
			</div>
		</div>
	</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",

  data: function () {
    return {
      username: "",
	  password: "",
	  userInput: {
		  username: "",
		  password: ""
	  }
    };
  },

  created: function () {
    let self = this;
  },

  methods: {
    abrirNuevoUsuario: function () {
      let self = this;
      self.userInput = {};
      const modal = new bootstrap.Modal(
        document.getElementById("modalRegistroUsuario")
      );
      modal.show();
    },

    getUser: function () {
      let self = this;

      axios
        .post(`http://localhost/graphql?`,{
			query: `
				query ($username:String!, $password:String!){
					userByUsernameAndPassword(username: $username, password: $password){
						id,
						user
					}
				}
			`,
			variables: {
				username: self.username,
				password: self.password
			}
		})
        .then((result) => {
         	console.log(result);
			let data = result.data;

      if(!data || data.data.userByUsernameAndPassword.length == 0) alert("Credenciales invalidas");
      else alert("Login exitoso");

			//let username = localStorage.getItem("current_username")
          	//this.$router.push({name: "user", params:{ username: username }})
        })
        .catch((error) => {
          console.log(error);
          console.log(typeof error);
          alert("ERROR de Servidor");
        });
    },

    postUser: function () {
      this.username = this.$route.params.username;
      let self = this;

	  axios
        .post(`http://localhost/user/`, {
			//grapql
		})
        .then((result) => {
          alert("¡Usuario registrado con exito!");
        })
        .catch((error) => {
          console.log(error);
          console.log(typeof error);
          alert("ERROR de Servidor");
        });
    }
  },
};
</script>

<style>
 .text-bold{
	 font-weight: 600;
 }
</style>
