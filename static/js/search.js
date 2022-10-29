$('.searchbox').keyup(function(e){
    const query = $('#search_key').val();
    $.ajax({
        dataType: 'json',
        url: '/api/word?search_key='+query,
        type: 'GET',
        success: (response) => {
            response = JSON.parse(response);
            if(response.status_code == 200 && response.status == 'success'){
                document.getElementById("words_list").innerHTML = '';
                for(var i=0; i<response.data.length; i++){
                    const result = response.data[i];
                    $('#words_list').append(`
                        <div style="cursor: pointer;" class="bg-white  mb-4 order-list shadow-sm">
                            <!-- <a style="text-decoration: none;" > -->
                                <div class="gold-members pl-4" onclick="location.href='/word?word_no=`+result[0]+`';">
                                    <div class="media">
                                        <div class="media-body pt-1 pb-1">
                                            <span class=" text-primary fw-normal text-lowercase"> 
                                                <i style="font-size: 12px; color: #ef6bffd8;" class="bi bi-chat-right-dots-fill fa-1x"></i>
                                                &nbsp;[`+result[2]+`]
                                            </span>
                                            <h5 class="text-black font-weight-bold">`+result[1]+`</h5>									
                                            <span class="text-gray"> `+result[3]+` </span>
                                        </div>
                                    </div>
                                </div>
                            <!-- </a> -->
                        </div>
                    `);
                }
            }
                
        
        }
    });
});