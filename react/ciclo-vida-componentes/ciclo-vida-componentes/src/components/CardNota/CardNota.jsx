import React, { Component } from "react";
import "./estilo.css";
//import deleteSVG from "../../assets/delete.svg"
//<img src={deleteSVG}/>
//importante que se for usar a imagem como componente então o nome do componente deve ser Maiusculo
//esse projeto foi criado com create-react-app mas se tivesse sido feito na mao eu poderia ter usado o SVGR para fazer essa "componetização"
import {ReactComponent as DeleteSVG} from "../../assets/delete.svg"

class CardNota extends Component {

  apagar(){
    const indice=this.props.indice
    this.props.apagarNota(indice)
  }

  render() {
    return (
      <section className="card-nota">
        <header className="card-nota_cabecalho">
          <h3 className="card-nota_titulo">{this.props.titulo}</h3>
          <DeleteSVG onClick={this.apagar.bind(this)}/>
          <h4>{this.props.categoria}</h4>
        </header>
        <p className="card-nota_texto">{this.props.texto}</p>
      </section>
    );
  }
}

export default CardNota;
