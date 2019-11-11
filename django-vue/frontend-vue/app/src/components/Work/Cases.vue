<template>
  <v-container>
      <div v-for="x in cases" v-bind:key="x.id">
        <p>{{x.name}}</p>
        
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteBook(x)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editBook(x)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
      </div>
      <CreateBooks @updateCases="all"></CreateBooks>
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
      cases: [],
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
          this.cases = response.data
          console.log(response)
        });
    },
    deleteBook(book) {
      if (confirm("Excluir " + book.name)) {
        axios
          .delete(`http://localhost:8000/api/books/${book.id}`, {
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
    editBook(book) {
      router.push(`/books/edit/${book.id}`)
    }
  }
};
</script>