// $('#word').keyup(function(e){
//     const query = $('#word').val();
//     $.ajax({
//         dataType: 'json',
//         url: '/api/word?search_key='+query,
//         type: 'GET',
//         success: (response) => {
//             response = JSON.parse(response);
//             if(response.status_code == 200 && response.status == 'success'){
//                 for(var i=0; i<response.data.length; i++){
//                     const result = response.data[i];
//                     $('#swords').append(`
//                         <li option="`+ result[1] +`">
//                     `);
//                 }
//             }
//         }
//     });
// });