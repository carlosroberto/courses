import React, { Component } from "react";
import ListaDeNotas from "./components/ListaDeNotas";
import FormularioCadastro from "./components/FormularioCadastro";
import ListaDeCategorias from "./components/ListaDeCategorias";
import "./assets/App.css";
import './assets/index.css';
import Categorias from "./Dados/Categorias";
import ArrayDeNotas from "./Dados/Notas";
class App extends Component {

  constructor() {
    super();

    this.categorias = new Categorias()
    this.notas = new ArrayDeNotas()
  
 // retirando this.state para que os dados sejam passados pelas classes acima, porem nao havera mais renderização em cascata
 //    this.state = {
 //     notas: [],
 //      categorias: [],
 //   }
  }
/*
  criarNota(titulo, texto, categoria) {
    const novaNota = { titulo, texto, categoria };
    const novoArrayNotas = [...this.state.notas, novaNota]
    const novoEstado = {
      notas: novoArrayNotas
    }
    this.setState(novoEstado)
  }

  deletarNota(index) {
    let arrayNotas = this.state.notas
    arrayNotas.splice(index, 1)
    this.setState({ notas: arrayNotas })
  }

  adicionarCategoria(nomeCategoria) {
    //adicionando nova categoria e depois adicionando o novo estado atual
    const novoArrayCategorias = [...this.state.categorias, nomeCategoria]
    const novoEstado = {...this.state, categorias:novoArrayCategorias} //estado atual + nova categoria
    this.setState(novoEstado)
  }
*/
  render() {
    return (
      <section className="conteudo">
        <FormularioCadastro 
        categorias={this.categorias.categorias}
        criarNota={this.notas.criarNota} />
        <main className="conteudo-principal">
          <ListaDeCategorias 
            adicionarCategoria={this.categorias.adicionarCategoria}
            categorias={this.categorias.categorias}
          />
          <ListaDeNotas
            apagarNota={this.notas.apagarNota}
            notas={this.notas.notas} 
          />
        </main>
      </section>
    );
  }
}

//new ListaDeNotas({notas:this.notas})
export default App;
