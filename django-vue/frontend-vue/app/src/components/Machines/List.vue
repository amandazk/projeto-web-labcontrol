<template>
  <v-container>
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
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="machines" :search="search">
      <template v-slot:items="props">
        <td>{{ props.item.name }}</td>
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


  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"

export default {
  name: "ListMachines",
  data() {
    return {
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
  }
};


</script>