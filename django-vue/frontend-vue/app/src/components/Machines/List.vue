<template>
  <v-container>
      <div v-for="machine in machines" v-bind:key="machine.id">
        <p>{{machine.name}}</p>
        <v-divider></v-divider>
      </div>

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