<template>
  <v-container>
    <h1>Edit Caso Info</h1>
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
 
      caso: {}
    }
  },
  computed: {
    nameErrors () {
      const errors = []
      if (!this.$v.caso.name.$dirty) return errors
      !this.$v.caso.name.maxLength && errors.push('Name must be at most 100 characters long')
      !this.$v.caso.name.required && errors.push('Name is required.')
      return errors
    },
    descriptionErrors () {
      const errors = []
      if (!this.$v.caso.description.$dirty) return errors
      !this.$v.caso.description.required && errors.push('Description is required')
      return errors
    },
  },
  methods: {
    getCaseInfo() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: `/api/work/get/${this.$route.params.id}/`
        })
        .then(res => {
          this.caso = res.data
          console.log(res)
        });
    },
    submit () {
      axios
        .put(
          `http://localhost:8000/api/work/edit/${this.$route.params.id}/`,
          this.caso, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(res => {
          route.push('/work/')
          console.log(res)
        });
    },
    clear () {
      route.push('/work/')
    },
  }
}
}
</script>