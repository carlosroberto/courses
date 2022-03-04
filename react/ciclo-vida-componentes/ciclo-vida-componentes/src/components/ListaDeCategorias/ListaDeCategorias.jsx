import React, { Component } from 'react'
import "./estilo.css"

class ListaDeCategorias extends Component {


    _handleEventoInput(e){
       if (e.key === "Enter"){
           let valorCategoria = e.target.value
           this.props.adicionarCategoria(valorCategoria)
       }
    }
    render() {
        return (
            <section className='lista-categorias'>
                <ul className='lista-categorias_lista'>
                    {this.props.categorias.map( (categoria, index) => {
                        return <li key={index} className='lista-categorias_item'>{categoria}</li>
                    })}
                </ul>
                <input type="text"
                    className='lista-categorias_input'
                    placeholder='Adicionar Categoria'
                    onKeyUp={this._handleEventoInput.bind(this)}
                />
            </section>
        )
    }

    /*
        <></>
    
    Com o lançamento da versão 16.x do React em 2017, o React disponibilizou o <React.Fragment> ou somente <Fragment>, que nos permite encapsular os elementos filhos sem ter que adicionar um novo elemento ao HTML.
    porém, este não se pode estilizar.
    */
}

export default ListaDeCategorias