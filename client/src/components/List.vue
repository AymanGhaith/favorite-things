<template>
  <div class="contatiner" id="fav-list">
    <div class="row">
      <div class="col-md-6 mx-auto">
        <h1 class="text-center">Favorite Things App</h1>
        <form v-on:submit.prevent="addNewFavThing">
          <label for="favtitleinput">Title</label>
          <input
            v-model="title"
            type="text"
            class="form-control"
            id="favtitleinput"
            placeholder="Add new favorite thing"
          />
          <label for="favdescinput">Description</label>
          <input
            v-model="description"
            type="text"
            class="form-control"
            id="favdescinput"
            placeholder="Add description"
          />
          <label for="favrankinginput">Ranking</label>
          <input v-model="ranking" type="number" class="form-control" id="favrankinginput" />
          <label for="favcategoryinput">Category</label>
          <select v-model="category" name="category" class="form-control" id="favrankinginput">
            <option
              v-for="(cat) in categories"
              v-bind:key="cat.id"
              v-bind:value="cat.id"
            >{{cat.name}}</option>
            <option>Add new Category</option>
          </select>
          <button
            v-if="this.isEdit == false"
            type="submit"
            class="btn btn-success btn-block mt-3"
          >Submit</button>
          <button
            v-else
            v-on:click="updateFavThing()"
            type="button"
            class="btn btn-primary btn-block mt-3"
          >Update</button>

          <table class="table">
            <tr v-for="(fav) in favthings" v-bind:key="fav.id" v-bind:title="fav.title">
              <td class="text-left">{{fav.title}}</td>
              <td class="text-right">
                <button
                  v-on:click="editFavThing(fav.title, fav.description, fav.category, fav.ranking, fav.id)"
                  type="button"
                  class="btn btn-info"
                >Edit</button>
                <button v-on:click="deleteFav(fav.id)" type="button" class="btn btn-danger">Delete</button>
              </td>
            </tr>
          </table>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  data () {
    return {
      categories: [],
      favthings: [],
      id: '',
      title: '',
      isEdit: false,
      description: '',
      ranking: 0,
      category: ''
    }
  },
  mounted () {
    this.getFavThings()
    this.getCategories()
  },
  methods: {
    clear () {
      this.title = ''
      this.description = ''
      this.category = ''
      this.ranking = 0
      this.isEdit = false
      this.description = ''
      this.ranking = 0
      this.category = ''
    },
    getFavThings () {
      this.$http
        .get(
          'http://favorite-things-eb.iejvb9fzxp.eu-west-2.elasticbeanstalk.com/favoriteThings'
        )
        .then(
          result => {
            console.log(result.data)
            this.favthings = result.data
          },
          error => {
            console.error(error)
          }
        )
    },
    getCategories () {
      this.$http
        .get(
          'http://favorite-things-eb.iejvb9fzxp.eu-west-2.elasticbeanstalk.com/categories'
        )
        .then(
          result => {
            console.log(result.data)
            this.categories = result.data
          },
          error => {
            console.error(error)
          }
        )
    },
    addNewFavThing () {
      this.$http.post('http://favorite-things-eb.iejvb9fzxp.eu-west-2.elasticbeanstalk.com/favoriteThings/', {
        title: this.title,
        description: this.description,
        category: this.category,
        ranking: this.ranking}).then(
        (res) => {
          this.clear()
          // this.title = ''
          // this.description = ''
          // this.category = ''
          // this.ranking = 0
          this.getFavThings()
          console.log(res)
        }
      ).catch(err => {
        console.error(err)
      })
    },
    editFavThing (title, description, category, ranking, id) {
      if (this.isEdit && this.id === id) {
        this.clear()
        return
      }
      this.id = id
      this.title = title
      this.description = description
      this.category = category
      this.ranking = ranking
      this.isEdit = true
    },
    updateFavThing () {
      this.$http.put(`http://favorite-things-eb.iejvb9fzxp.eu-west-2.elasticbeanstalk.com/favoriteThings/${this.id}/`, {
        title: this.title,
        description: this.description,
        category: this.category,
        ranking: this.ranking}).then(
        res => {
          this.clear()
          // this.title = ''
          // this.description = ''
          // this.category = ''
          // this.ranking = 0
          // this.isEdit = false
          this.getFavThings()
          console.log(res)
        }).catch(
        err => {
          console.error(err)
        })
    },
    deleteFav (id) {
      this.$http.delete(`http://favorite-things-eb.iejvb9fzxp.eu-west-2.elasticbeanstalk.com/favoriteThings/${id}/`).then(
        res => {
          this.clear()
          // this.title = ''
          // this.description = ''
          // this.ranking = 0
          // this.category = ''
          this.getFavThings()
          console.log(res)
        }).catch(
        err => {
          console.error(err)
        })
    }
  }
}
</script>
