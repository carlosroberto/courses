import React, { Component } from "react";
import CardNota from "../CardNota";
import "./estilo.css";
class ListaDeNotas extends Component {

  //como nao criamos mais propriedades especificas senao usá-lo para passagem de props entao o construtor é desnecessario, a informação será passada para o elemento pai do Component
  // o this.props la embaixo basta.
  // constructor(props){
  //   super(props)
  // }

  render() {
    return (
      <ul className="lista-notas">
        {this.props.notas.map((nota, index) => {
          return (
            <li className="lista-notas_item" key={index}>
              <CardNota titulo={nota.titulo} texto={nota.texto}/>
            </li>
          );
        })}
      </ul>
    );
  }
}

export default ListaDeNotas;
