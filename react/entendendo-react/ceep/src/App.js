import React, { Component } from "react";
import ListaDeNotas from "./components/ListaDeNotas";
import FormularioCadastro from "./components/FormularioCadastro";
import "./assets/App.css";
import './assets/index.css';
class App extends Component {

  constructor(){
    super()
//    this.notas = []
    this.state = {
      notas: []
    } //gerenciado pelo react
  }


  // criarNota(titulo, texto){
  //   const novaNota = {titulo, texto}
  //   this.notas.push(novaNota)
  //   //passar para react qual é o novo estado do objeto, 
  //   //"atualize o estado interno deste componente "App" para que o estado notas dele seja compativel com o atributo this.notas que sofreu um push de um item no array "
  //   //se eu comentar  this.notas.push(novaNota) e tentar criar a nota ele nao vai re-renderizar apesar do setState abaixo porque nada mudou
  //   this.setState({
  //     notas:this.notas
  //   }) 
  // }

  criarNota(titulo, texto){
    const novaNota = {titulo, texto}
    const novoArrayNotas = [...this.state.notas,novaNota]
    const novoEstado = {notas: novoArrayNotas}
    this.setState(novoEstado) 
  }

  render() {
    return (
      <section className="conteudo">
        <FormularioCadastro  criarNota={this.criarNota.bind(this)}/>
        <ListaDeNotas notas={this.state.notas}/>
      </section>
    );
    //formularioCadastro recebe um propriedade personalizada do react que chamei de criarNota, 
    //la no construtor do FormularioCadastro eu mando um famoso "props" (propriedades segundo a comunidade, mas o jsx chama atributo) de forma que consigamos acessar elas diretamente
  }
}

//     <ListaDeNotas notas={this.state.notas}/> é igual a new ListaDeNotas({notas:this.notas})

export default App;
