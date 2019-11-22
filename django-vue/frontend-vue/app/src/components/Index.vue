<template>
  <section class="container">
    <h1>ACE - Estágio não obrigatório</h1>
    <p></p>
    <!-- <p>O estágio na instituição ACE é realizado no laboratório de informática e o controle das máquinas é uma 
      das tarefas executadas. Para isso, esse site cuida do cadastro de problemas que ocorrem e também, quando
      necessário, do cadastro de novas máquinas.</p> -->
      <!-- <div class="my-2">
        <v-btn small color="green" v-if="authenticated">Logout</v-btn>
      </div> -->
        <div class="row">
          <div class="col s12 m6">
           <div class="card light-green lighten-4">
            <div class="card-content">
            <p>O estágio na instituição ACE é realizado no laboratório de informática e o controle das máquinas é uma 
              das tarefas executadas. Para isso, esse site cuida do cadastro de problemas que ocorrem e também, quando
              necessário, do cadastro de novas máquinas.</p>
          </div>
      </div>
    </div>
  </div>
          
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