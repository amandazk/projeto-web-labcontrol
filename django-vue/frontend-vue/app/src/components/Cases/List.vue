<template>
  <v-container>
      <div v-for="caso in casos" v-bind:key="caso.id">
        <p>{{caso.problemname}}</p>
        <p>{{caso.machinename}}</p>

        
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteCase(caso)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editCase(caso)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
      </div>
      <CreateCases @updateCases="all"></CreateCases>

    <!-- <v-card>
    <v-card-title>
      <h4>Casos</h4>
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="machines.name"
    ></v-data-table>
  </v-card> -->


  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateCases from "./Create";

export default {
  name: "ListCases",
  data() {
    return {
      casos: [],
    };
  },
  components: {
    CreateCases: CreateCases,
  },
  created() {
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/work/"
        })
        .then(response => {
          this.casos = response.data
          console.log(response)
        });
    },
    deleteCases(caso) {
      if (confirm("Excluir " + caso.name)) {
        axios
          .delete(`http://localhost:8000/api/cases/${caso.id}`, {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          })
          .then(response => {
            this.all()
            console.log(response)
          });
      }
    },
    editCases(caso) {
      router.push(`/cases/edit/${caso.id}`)
    }
  }
};
</script>