<template>
  <v-container>
      <!-- <div v-for="caso in casos" v-bind:key="caso.id">
        <p>{{caso.problemname}}</p>
        <p>{{caso.machinename}}</p> -->

    <v-card>
    <v-card-title>
      <h4>Problemas do Lab</h4>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Pesquisa"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="problemname" :search="search">
      <template v-slot:items="props">
        <td>{{ props.item.name }}</td>
        <td class="text-xs-right">{{ props.item.problemname }}</td>
        <td class="text-xs-right">{{ props.item.machines }}</td>
        <!-- <td class="text-xs-right">{{ props.item.fat }}</td>
        <td class="text-xs-right">{{ props.item.carbs }}</td>
        <td class="text-xs-right">{{ props.item.protein }}</td>
        <td class="text-xs-right">{{ props.item.iron }}</td> -->
      </template>
      <!-- <template v-slot:pageText="props">
      ITEMS {{ props.pageStart }} - {{ props.pageStop }} OF {{ props.itemsLength }} // Edit this
      // ^this is what you need
      </template> -->
    </v-data-table>
  </v-card>


        
        <!-- <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteCase(caso)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editCase(caso)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
      </div>
      <CreateCases @updateCases="all"></CreateCases> -->



  </v-container>
</template>
<style>
  h4{
    text-align:center;
    color:#6b6b47;
    };

</style>


<script>
import axios from "axios";
import router from "@/router/"
import CreateCases from "./Create";

export default {
  name: "ListCases",
  data() {
    return {
      casos: [],
      problemname: [],
      machines: [],
      search: '',
      headers: [
        {
          text: 'Problema',
          align: 'left',
          sortable: false,
          value: 'name',
        },
        {
          text: 'Máquina',
          align: 'left',
          sortable: false,
          value: 'name',
        },
      ],
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
    deleteCase(caso) {
      if (confirm("Excluir esse caso? ")) {
        axios
          .delete(`http://localhost:8000/api/work/${caso.id}`, {
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
    editCase(caso) {
      router.push(`/listcases/edit/${caso.id}`)
    }
  }
};
</script>