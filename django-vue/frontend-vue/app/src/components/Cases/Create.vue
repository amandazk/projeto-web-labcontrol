<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-card-text>
          <v-fab-transition>
            <v-btn green v-on="on" dark relative fixed bottom right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </template>

      <v-card>
        <v-card-title>
          <span class="headline">Adicionar Casos</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-select
                  :items = "problems"
                  item-value = "id"
                  item-text = "problem"
                  label = "Problems"
                  attach
                  single-line
                  v-model = "caso.problem"
                >
                </v-select>
              </v-col>
              <v-col cols="12">
                <v-select
                  :items = "machines"
                  item-value = "id"
                  item-text = "name"
                  label = "Machine"
                  attach
                  v-model = "caso.machine"
                >
                </v-select>
              </v-col>
            </v-row>

          </v-container>
          <small>*informações obrigatórias</small>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="green" text @click="dialog = false">Fechar</v-btn>
          <v-btn color="green" text @click="add()">Salvar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>

</template>
<script>
import axios from "axios"
export default {
  name: "CreateCases",
  data() {
    return {
      dialog: false,
      caso: {},
      machines: [],
      problems: []
    };
  },
  created() {
    this.getProblems()
    this.getMachines()
  },
  methods: {
    getProblems() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/work/problem/"
      })
      .then(response => {
        this.problems = response.data
        console.log(response)
      });
    },
    getMachines() {
      axios
      .request({
        baseURL: "http://localhost:8000",
        method: "get",
        url: "/api/work/machines/"
      })
      .then(response => {
        this.machines = response.data
        console.log(response)
      });
    },
     add() {
       axios
         .post("http://localhost:8000/api/work/add/",
           this.caso,
           {
             headers: {
               Authorization: `Token ${this.$session.get("token")}`
             }
           }
         )
         .then(response => {
           this.dialog = false
           this.$emit('updateCases')
           this.log.console(response)
         });
    },
  }
  };
</script>



