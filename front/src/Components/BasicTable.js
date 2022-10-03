import "./BasicTable.css"

function BasicTable(props) {
  return (
    <table className="container">
      <thead>
        <tr>
          <th>Algoritmo</th>
          <th>Tiempo</th>
          <th>Memoria</th>
          <th>Dimension Laberinto</th>
        </tr>
      </thead>
      <tbody>
      {props.rows.map((row) => (
        <tr key={row.memory}>
          <td>{row.alg}</td>
          <td>{row.time}</td>
          <td>{row.memory}</td>
          <td>{row.shape}</td>
        </tr>
    ))}
      </tbody>
    </table>
  );
}

export default BasicTable;