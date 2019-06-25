var load = document.querySelector('.load');
var sub = document.querySelector('.submit');
var pr = document.querySelector('#pr');
var ps=document.querySelector('#ps');
sub.addEventListener('click',function(e){
     load.style.display='block'
     sub.style.display='none'
     pr.style.display='none'
     ps.style.display='none'
})
var inpq=document.querySelector('#inp-q');
var inpr=document.querySelector('#inp-r');
var inps=document.querySelector('#inp-s');
inpq.addEventListener('keyup',function(e){
  var p=document.querySelector('#rq');
  p.textContent=e.target.value
})
inpr.addEventListener('keyup',function(e){
  var p=document.querySelector('#rr');
  p.textContent=e.target.value
})
inps.addEventListener('keyup',function(e){
  var p=document.querySelector('#rs');
  p.textContent=e.target.value
})
var res= document.querySelector('#res');
console.log(res.textContent)
