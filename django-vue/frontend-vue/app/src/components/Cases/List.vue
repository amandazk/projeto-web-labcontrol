
<template>
  <div>
    <p></p>
    <v-col cols="12"><h4>Problemas do Lab por Máquina</h4></v-col>
    <v-simple-table
      :dense="dense"
      :fixed-header="fixedHeader"
      :height="height"
    >
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Problema</th>
            <th class="text-left">Máquina</th>
          </tr>
        </thead>
        <tbody>

          <tr v-for="caso in casos" v-bind:key="caso.id">
            <td>{{caso.problemname}}</td>
            <td>{{caso.machinename}}</td>
            <!-- <v-btn class="ma-2" text icon color="green">
              <v-icon class="edit" @click="editCase(caso)"></v-icon>
           </v-btn> -->
            <v-btn class="ma-2" text icon color="red lighten-2">
              <v-icon class="delete" @click="deleteCase(caso)"></v-icon>
           </v-btn>
          </tr>



        </tbody>
      </template>
    </v-simple-table>

   <CreateCases @updateCases="all"></CreateCases>
  </div>
</template>
<style>
  h4{
    text-align:left;
    color:#6b6b47;
    font-size: 20px;
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
      authenticated: false,
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
  mounted() {
    this.checkAuthenticated();
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
