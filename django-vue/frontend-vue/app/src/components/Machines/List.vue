<template>
  <v-container>
      <!-- Mostrando sem a tabela -->
      <!-- <div v-for="machine in machines" v-bind:key="machine.id">
        <p>{{machine.name}}</p>
        <v-divider></v-divider>
      </div> -->

  
  <v-card>
    <v-card-title>
      <h4>Máquinas do Lab</h4>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Pesquisa"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="machines" :search="search">
      <template v-slot:items="props">
        <td>{{ props.item.name }}</td>
        <td class="text-xs-right">{{ props.item.machines }}</td>
      </template>
    </v-data-table>
  </v-card>


  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"

export default {
  name: "ListMachines",
  data() {
    return {
      authenticated: false,
      machines: [],
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
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/work/machines"
        })
        .then(response => {
          this.machines = response.data
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
