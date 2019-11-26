      
<template>
  <div>
    <p></p>
    <h4>Problemas do Lab</h4>
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
          </tr>

        </tbody>
      </template>
    </v-simple-table>

    <!-- <v-row>
      <v-col cols="12" md="6">
        <v-text-field
          v-model="height"
          class="mx-4"
          label="Height - px"
          max="500"
          min="1"
          step="1"
          style="width: 125px"
          type="number"
          @keydown="false"
        ></v-text-field>
      </v-col>
    </v-row> -->

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