<template>
  <v-container>
      <!-- Mostrando sem a tabela -->
      <p></p>
      <h4>Problemas</h4>
      <p></p>
      <div v-for="problem in problems" v-bind:key="problem.id">
        <p><b>Problema:</b> {{problem.problem}}</p>
        <p><b>Descrição:</b> {{problem.description}}</p>
        <v-divider></v-divider>
      </div>

    <CreateProblem @updateProblem="all"></CreateProblem>
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateProblem from "./Create";


export default {
  name: "ListProblems",
  data() {
    return {
      authenticated: false,
      problems: [],
      search: '',
      headers: [
        {
          text: 'Nome',
          align: 'left',
          sortable: false,
          value: 'name',
        },
      ],
    };
  },
  created() {
    this.all();
  },
  mounted() {
    this.checkAuthenticated();
  },
  components: {
        CreateProblem: CreateProblem,
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/work/problem"
        })
        .then(response => {
          this.problems = response.data
          console.log(response)
        });
    },
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
