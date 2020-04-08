/* ========================= Add Accounting Note ========================= */
$('#add-row').click(function() {
  var form_idx = $('#id_{{ formset.prefix }}-TOTAL_FORMS').val();
  form_cloned = $('<div>').append($('.formset-template').clone()).html().replace(/formset-template/g, '');
  form_cloned = form_cloned.replace(/__prefix__/g, form_idx);
  $('#formset_table tbody').append(form_cloned);
  $('#{{ formset.prefix }}-' + form_idx).show();
  $('#id_{{ formset.prefix }}-TOTAL_FORMS').val(parseInt(form_idx) + 1);

  $("#formset_table tbody tr:visible").each(function (index) {
    $(this).css("background-color", !!(index & 1)? "inherit" : "rgba(0,0,0,.05");
  });

  var datepickerDict = {};
  var isBootstrap4 = $.fn.collapse.Constructor.VERSION.split('.').shift() == "4";
  $("[dp_config]:not([disabled])").each(function (i, element) {
      var $element = $(element), data = {};
      try {
          data = JSON.parse($element.attr('dp_config'));
      }
      catch (x) { }
      if (data.id && data.options) {
          data.$element = $element.datetimepicker(data.options);
          data.datepickerdata = $element.data("DateTimePicker");
          datepickerDict[data.id] = data;
          data.$element.next('.input-group-addon').on('click', function(){
              data.datepickerdata.show();
          });
          if(isBootstrap4){
              data.$element.on("dp.show", function (e) {
                  $('.collapse.in').addClass('show');
              });
          }
      }
  });
  if(isBootstrap4) {
      $('body').on('show.bs.collapse','.bootstrap-datetimepicker-widget .collapse',function(e){
          $(e.target).addClass('in');
      });
      $('body').on('hidden.bs.collapse','.bootstrap-datetimepicker-widget .collapse',function(e){
          $(e.target).removeClass('in');
      });
  }
});


/* ======================= Remove Accounting Note ======================= */
$(document).on('click', '[id^="{{ formset.prefix }}-DELETE-"]', function(e){
  var id = '#id_' + $(this).closest("tr").attr('id') + '-DELETE';
  $(id).val("true")
  $(this).closest("tr").hide();

  $("#formset_table tbody tr:visible").each(function (index) {
    $(this).css("background-color", !!(index & 1)? "inherit" : "rgba(0,0,0,.05");
  });
});