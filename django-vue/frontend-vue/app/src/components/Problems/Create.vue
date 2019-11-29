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
          <span class="headline">Adicionar Problemas</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="problem.problem" label="Problema*" hint="Escreva seu problema" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="problem.description" label="Descrição*" type="text" required></v-text-field>
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
  name: "CreateProblems",
  data() {
    return {
      dialog: false,
      problem: {}
    };
  },
  methods: {
     add() {
       axios
         .post("http://localhost:8000/api/work/problem/add/",
           this.problem,
           {
             headers: {
               Authorization: `Token ${this.$session.get("token")}`
             }
           }
         )
         .then(response => {
           this.dialog = false
           this.$emit('updateProblem')
           this.log.console(response)
         });
    },
  }
  };
</script>



