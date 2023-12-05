import React, { Component } from 'react';

class ListaDeItens extends Component {
  constructor(props) {
    super(props);
    this.state = {
      itens: ['Item 1', 'Item 2', 'Item 3'],
      novoItem: '',
    };
  }

  adicionarItem = () => {
    if (this.state.novoItem.trim() !== '') {
      this.setState((prevState) => ({
        itens: [...prevState.itens, prevState.novoItem],
        novoItem: '',
      }));
    }
  };

  handleChange = (event) => {
    this.setState({ novoItem: event.target.value });
  };

  render() {
    return (
      <div>
        <h1>Lista de Itens</h1>
        <ul>
          {this.state.itens.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
        <input
          type="text"
          value={this.state.novoItem}
          onChange={this.handleChange}
        />
        <button onClick={this.adicionarItem}>Adicionar Item</button>
      </div>
    );
  }
}

export default ListaDeItens;
