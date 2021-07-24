<template>
    <div id="Categories">
        <h2>Usuario autenticado: <span>{{username}}</span></h2>
        <div>
            <h4>Registrar Categoría</h4>
            <input name='categoria_name' type='text 'v-model="categoriaInput.name" placeholder='Nombre'>
            <input name='categoria_description' type='text' v-model="categoriaInput.description" placeholder="Descripción">
            <button v-on:click="postCategory">Guardar</button>
        </div>
        <label for='CategoriaId'>Categoria Id</label>
        <input name='CategoriaId' type='number'v-model="categoriaId" placeholder='Digite un Id Valido'>
        <button v-on:click="getCategory">Obtener categoría</button>
        <h2>La categoría con id = <span>{{category_id}}</span>, tiene el nombre <span>{{name}}</span> y su descripción es «<span>{{description}}</span>».</h2>
    </div>
</template>

<script>

    import axios from 'axios';

    export default {

        name: 'Categories',

        data: function (){
            return {
                category_id: "",
                name: "",
                description: "",
                categoriaId: 1,
                categoriaInput: {
                    name: '',
                    description: ''
                },
                mensaje: ""
            }
        },

        created: function() {

            this.username = this.$route.params.username
            let self = this

        },

        methods: {

            getCategory: function() {

                this.username = this.$route.params.username
                let self = this

                axios.get(`http://localhost:4000/categories/${self.categoriaId}`)
                    .then((result) => {
                        self.category_id = result.data.id,
                        self.name = result.data.name,
                        self.description = result.data.description
                    })
                    .catch((error) => {
                        console.log(error);
                        console.log(typeof error);
                        alert("ERROR de Servidor");
                    });
            },

            postCategory: function() {

                this.username = this.$route.params.username
                let self = this
                console.log(self.categoriaInput);
                axios.post(`http://localhost:4000/categories`, self.categoriaInput)
                    .then((result) => {
                        console.log(result);
                        self.mensaje = "Categoria Registrada Correctamente";
                    })
                    .catch((error) => {
                        console.log(error);
                        console.log(typeof error);
                        alert("ERROR de Servidor");
                    });
            }
        }
    }
</script>

<style>
    #Categories{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    #Categories h2{
        font-size: 25 px;
        color: #283747;
    }
    #Categories span{
        color: crimson;
        font-weight: bold;
    }
</style>
