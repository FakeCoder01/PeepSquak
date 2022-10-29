

function downloadPDFfile(){
    let pdfFileHTML = `
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>PeepSquak</title>
            <style>
                table, th, td {
                    border: 2px solid rgb(57, 109, 206);
                    border-collapse: collapse;
                    padding: 8px;
                }
                .center{
                    text-align: center;
                    font-size: 17px;
                    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
                }
                .td1{
                    width: 28%;
                }
                .td2{
                    width : 32%;
                }
                .td3{
                    width : 40%;
                }
                thead tr{
                    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                    font-size: 20px;
                }
            </style>
        </head>
        <body>
            <div class="download-table">
                <table style="width: 100%;">
                    <thead>
                        <tr>
                            <th>Russian Word</th>
                            <th>Meaning in English</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody id="updatePDFWordList">
    `;
    $.ajax({
        dataType: 'json',
        url: '/api/word?search_key=',
        type: 'GET',
        
        success: (response) => {
            response = JSON.parse(response);
            if(response.status_code == 200 && response.status == 'success'){
                for(var i=0; i<response.data.length; i++){
                    const result = response.data[i];
                    pdfFileHTML += ` 
                        <tr>
                        <td class="center td1"><span style="font-size: 18px;">` +
                        result[1]+`</span> <br> [<span style="color: rgb(70, 125, 196);">
                        ` +
                        result[2]+`
                        </span>] </td>
                        <td class="center td2">` +
                        result[3]+`</td>
                        <td class="desc td3">` +
                        result[0]+`. ` +
                        result[4]+`</td>
                        </tr>
                    `;
                }
            }
            pdfFileHTML +=` 
                    </tbody>
                        </table>
                    </div>
                </body>
                </html>
            `;
                
            var printPDFile = window.open('', '', 'height=400,width=800');
            printPDFile.document.write(pdfFileHTML);
            printPDFile.print()

        }
    });
}