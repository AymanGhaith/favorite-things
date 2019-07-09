<template>
  <div class="contatiner" id="fav-list">
    <div class="row">
      <div class="col-md-6 mx-auto">
        <h1 class="text-center">
          Favorite Things App
        </h1>
        <form v-on:submit.prevent="addNewFavThing">
          <label for="favtitleinput">Title</label>
          <input v-model="title" type="text" class="form-control" id="favtitleinput" placeholder="Add new favorite thing">
          <label for="favdescinput">Description</label>
          <input v-model="description" type="text" class="form-control" id="favdescinput" placeholder="Add description">
          <label for="favrankinginput">Ranking</label>
          <input v-model="ranking" type="number" class="form-control" id="favrankinginput">
          <label for="favcategoryinput">Category</label>
          <select v-model="category" name="category" class="form-control" id="favrankinginput">
            <option v-for="(cat) in categories" v-bind:key="cat.id" v-bind:category="cat.name"> {{cat.name}}</option>
            <option>Add new Category</option>
          </select>
          <button v-if="this.isEdit == false" type="submit" class="btn btn-success btn-block mt-3">
            Submit
          </button>
          <button v-else v-on:click="updateFavThing()" type="button" class="btn btn-primary btn-block mt-3">
            Updatefavthings
          </button>

          <table class="table">
            <tr v-for="(fav) in favthings" v-bind:key="fav.id" v-bind:title="fav.title">
              <td class="text-left"> {{fav.title}} </td>
              <td class="text-right">
                <button v-on:click="editFavThing(fav.title,fav.id)" type="button" class="btn btn-info"> Edit </button>
                <button v-on:click="deleteFav(fav.id)" type="button" class="btn btn-danger"> Delete </button>
              </td>
            </tr>
          </table>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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
    getCategories () {
      axios({method: 'GET', url: '/categories'}).then(
        result => {
          console.log(result.data)
          this.categories = result.data
        },
        error => {
          console.error(error)
        }
      )
    },
    getFavThings () {
      axios({method: 'GET', url: '/favoriteThings'}).then(
        result => {
          console.log(result.data)
          this.favthings = result.data
        },
        error => {
          console.error(error)
        }
      )
    },
    addNewFavThing () {
      debugger
      axios.post('/favoriteThings', {title: this.title}).then(
        (res) => {
          this.title = ''
          this.getFavThings()
          console.log(res)
        }
      ).catch(err => {
        console.error(err)
      })
    },
    editFavThing (title, id) {
      this.id = id
      this.title = title
      this.isEdit = true
    },
    updateFavThing () {
      axios.put(`/favoriteThings/${this.id}`, {title: this.title}).then(
        res => {
          this.title = ''
          this.isEdit = false
          this.getFavThings()
          console.log(res)
        }).catch(
        err => {
          console.error(err)
        })
    },
    deleteFav (id) {
      axios.delete(`/favoriteThings/${this.id}`).then(
        res => {
          this.title = ''
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
