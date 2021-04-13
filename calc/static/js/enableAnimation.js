$(function(){
var tooltipTriggerList = [].slice.call($('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
})

$(function(){
  var tooltip=new bootstrap.Tooltip({
      trigger: 'hover click focus',
      container: 'body',
      boundary: 'window'
  })
});

$(function(){
var popoverTriggerList = [].slice.call($('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})
})

$(function(){
var popover = new bootstrap.Popover($('.popover-dismiss'),{
  trigger: 'focus'
})
})