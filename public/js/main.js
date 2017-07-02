$(function() {

  // Inject the datepicker
  $("#id_reservation_date").attr("type", "date").addClass("datepicker");
  // Inject the timepicker
  $("#id_reservation_hour").attr("type", "date").addClass("timepicker");

  $('.datepicker').pickadate({
      selectMonths: true,
      selectYears: 5,
      monthsFull: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
      weekdaysShort: ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam'],
      today: 'aujourd\'hui',
      clear: 'effacer',
      format: 'yyyy-mm-dd',
      formatSubmit: 'yyyy-mm-dd'
  });


  $('.timepicker').pickatime({
    default: 'now', // Set default time
    fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
    twelvehour: false, // Use AM/PM or 24-hour format
    donetext: 'OK', // text for done-button
    cleartext: 'Effacer', // text for clear-button
    canceltext: 'Annuler', // Text for cancel-button
    autoclose: false, // automatic close timepicker
    ampmclickable: true, // make AM PM clickable
    aftershow: function(){} //Function for after opening timepicker
  });

});