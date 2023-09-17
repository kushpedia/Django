
let searchform = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')
if (searchform){
    for (let i=0; i< pageLinks.length; i++){
        pageLinks[i].addEventListener('click', function(e){
            e.preventDefault()
            // get the data attribute
            let page=this.dataset.page
            // add input field in the search form
            searchform.innerHTML += `<input value=${page} name="page" hidden />`
            
            // submit the search form
            searchform.submit()

        })
    }
}


