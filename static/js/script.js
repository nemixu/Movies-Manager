const user_input = $('#user_input')
const apikey = "3c0dea9f";
let url = `http://www.omdbapi.com/?apikey=${apikey}&s=Batman`;

const fetchMovies = () => {
    fetch(url)
    .then(result => result.json())
    .then(data => {
        console.log(data)
    })
}
fetchMovies();