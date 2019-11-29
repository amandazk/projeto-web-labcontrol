<template>
  <section class="container">
    <h1>LabControl</h1>
    <p></p>
        <div class="row">
          <div class="col s12 m6">
           <div class="card light-green lighten-4">
            <div class="card-content">
            <p>Com diversas máquinas para fazer a manutenção, é importante ter um meio de controle e organização.
              Com o LabControl é possível cadastrar novos problemas, editá-los, excluí-los e também, ter um registro
              de todas as máquinas disponíveis no laboratório. 
            </p>
          </div>
      </div>
    </div>
  </div>



  <v-row align="center" justify="center">
    <v-img
      src="https://img.ibxk.com.br/2016/12/16/16184004311314.jpg?w=1120&h=420&mode=crop&scale=both"
      aspect-ratio="1"
      class="grey lighten-2"
      max-width="500"
      max-height="300"
    ></v-img>
  </v-row>


  <div class="row">
          <div class="col s12 m6">
           <div class="card light-green lighten-4">
            <div class="card-content">
            <p></p>
            <p> * O próximo passo será criar uma área para cadastrar novos problemas e também botões para editar
              e excluir os casos já existentes. 
            </p>
          </div>
      </div>
    </div>
  </div>


  <!-- <v-row align="center" justify="center">
    <v-img
      src="https://img.ibxk.com.br/2016/12/16/16184004311314.jpg?w=1120&h=420&mode=crop&scale=both"
      aspect-ratio="1"
      class="grey lighten-2"
      max-width="500"
      max-height="300"
    ></v-img>
  </v-row> -->

  <!-- <v-carousel hide-delimiters>
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
    ></v-carousel-item>
  </v-carousel> -->

  </section>

   
</template>
<style>
  h1{
    text-align:center;
    color:#6b6b47;
    };
  .card-content{
    text-align:justify;
    color:#6b6b47;
  }
</style>


<script>
import router from "../router";

export default {
  name: "Index",
  data() {
    return {
      authenticated: false
    };
  },
  mounted() {
    this.checkAuthenticated();
  },
  methods: {
    checkAuthenticated() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      } else {
        this.authenticated = true;
      }
    }
  }
};

</script>

