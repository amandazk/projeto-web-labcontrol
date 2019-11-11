<template>
  <v-container>
    <h1>Edit Book Info</h1>
    <form>
      <v-text-field
        v-model="caso.name"
        :error-messages="nameErrors"
        :counter="100"
        label="Name"
        required
        @input="$v.caso.name.$touch()"
        @blur="$v.caso.name.$touch()"
      ></v-text-field>

      <v-btn class="mr-4" @click="submit">Submit</v-btn>
      <v-btn @click="clear">Clear</v-btn>
    </form>
  </v-container>
</template>

<script>
import axios from "axios"
import route from "@/router/"
import { validationMixin } from 'vuelidate'

import { required, maxLength } from 'vuelidate/lib/validators'

export default {
  name: 'EditCase',
  created () {
    this.getCasoInfo()
  },
  mixins: [validationMixin],

  validations: {
    caso: {
      name: {
        maxLength: maxLength(100),
        required
      },
  },

  data () {
    return {
      name: "",
      author: "",
      description: "",
      book: {}
    }
  },
  computed: {
    nameErrors () {
      const errors = []
      if (!this.$v.book.name.$dirty) return errors
      !this.$v.book.name.maxLength && errors.push('Name must be at most 100 characters long')
      !this.$v.book.name.required && errors.push('Name is required.')
      return errors
    },
    authorErrors () {
      const errors = []
      if (!this.$v.book.author.$dirty) return errors
      !this.$v.book.author.required && errors.push('Author is required')
      return errors
    },
    descriptionErrors () {
      const errors = []
      if (!this.$v.book.description.$dirty) return errors
      !this.$v.book.description.required && errors.push('Description is required')
      return errors
    },
  },
  methods: {
    getBookInfo() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: `/api/books/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.book = res.data
          console.log(res)
        });
    },
    submit () {
      axios
        .put(
          `http://localhost:8000/api/books/edit/${this.$route.params.id}/`,
          this.book, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          route.push('/books/')
          console.log(res)
        });
    },
    clear () {
      route.push('/books/')
    },
  }
}
</script>