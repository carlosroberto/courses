export default class Categorias{
    
    constructor(){
        this.categorias = []
        this._inscritos = [] //quem sao os inscritos?
    }

    inscrever(func){
        this._inscritos.push(func)
    }

    //para cada inscrito eu executo a função que recebi
    notificar(){
        this._inscritos.forEach(func =>{
            func(this.categorias)
        })
    }

    adicionarCategoria(novaCategoria) {
        
        this.categorias.push(novaCategoria)

    }
}