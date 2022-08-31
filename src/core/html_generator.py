def get_html_report(result, counts, file_name, time, rows):
    return (
        """<html>
    <head>
        <style>
        html, body {
            min-height: 100%;
        }
        body{
            font-family: 'Roboto';
            background-color: #fff;
            padding: 50px;
        }
        .container{
            width: 80%;
            margin-left:auto;
            margin-right:auto;
            border: 1px solid #eee;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.10),
                0px 10px 20px rgba(0,0,0,0.05),
                0px 20px 20px rgba(0,0,0,0.05),
                0px 30px 20px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            padding: 20px;
        }
        .results-cont{ display: flex;flex-direction: row;}
        .inside-container{ width: 50%;}
        .inside-container-full{ width: 100%; text-align: center;}
        table{
            width: 100%;
            padding: 10px;
            background-color: #fff;
            text-align: left;
        }
        th{
            color: #666666;
            font-size: 12px;
            font-weight: normal;
            text-transform: uppercase;
            border-color: #fff;
        }
        td{
            padding: 5px 10px;
            font-size: 14px;
            border: solid 1px #666666;
            border: 1px solid #eee;
        }
        th,td{
            border-collapse: collapse;
        }
        h1{
            margin: 10px;
            width: 100%;
            text-align: left;
        }
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>Execution results - <file></h1>
            <div class='inside-container-full'>
                <table>
                    <tr>
                        <th><b>File Processed</b></th>
                        <th><b>Rows</b></th>
                        <th><b>Time Spent</b></th>
                    </tr>
                    <tr>
                        <td><file></td>
                        <td><rows></td>
                        <td><time></td>
                    </tr>
                </table>
            </div>
            <div class='inside-container-full'>
                <table>
                        <tr>
                            <th><b>Distincts</b></th>
                        </tr>
                        <tbody>
                            <distincts>
                        </tbody>
                </table>
            </div>
            <div class="results-cont">
                <div class='inside-container'>
                    <table>
                        <tr>
                            <th><b>Full Names Occurrences</b></th>
                        </tr>
                        <tbody>
                            <full_names>
                        </tbody>
                    </table>
                </div>
                <div class='inside-container'>
                    <table>
                        <tr>
                            <th><b>Last Names Occurrences</b></th>
                        </tr>
                        <tbody>
                            <last_names>
                        </tbody>
                    </table>
                </div>
                 <div class='inside-container'>
                    <table>
                        <tr>
                            <th><b>Names Occurrences</b></th>
                        </tr>
                        <tbody>
                            <names>
                        </tbody>
                    </table>
                </div>
                <div class='inside-container'>
                    <table>
                        <tr>
                            <th><b>List of modified names</b></th>
                        </tr>
                        <tbody>
                            <results>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
</html>""".replace(
            "<counts>", str(counts)
        )
        .replace("<results>", result)
        .replace("<distincts>", counts["distincts"])
        .replace("<full_names>", counts["full_names"])
        .replace("<last_names>", counts["last_names"])
        .replace("<names>", counts["names"])
        .replace("<file>", file_name)
        .replace("<rows>", str(rows))
        .replace("<time>", str(time))
    )
