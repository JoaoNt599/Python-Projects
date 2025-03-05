const axios = require ('axios');
const hostPath = 'http://localhost:5000';

(async () => {
    let response;
    try {
        response = await axios.get (`${hostPath}/`);
    } catch (error) {
        console.log('Not possible to get cpf path', error);
        process.exit(1);
    }

    const queryPath = response?.data?._links?.pessoas?.obterPessoasPeloCPF;
    const cpfPath = queryPath.replace("<string:cpf>", "");
    ['35681193071', '45678912321', '111000'].forEach (cpf => {
        axios.get(`${hostPath}${cpfPath}/${cpf}`)
             .then (response => {
                 console.log (response.data);
             })
             .catch (error => {
                 console.log (error?.response?.data);
             });
    });
})();