const TableRow = (props) => {
  return (
    <tr>
      <td>{props[props.group] ? props[props.group] : "Unknown"}</td>
      <td>{props.open}</td>
      <td>{props.view}</td>
      <td>{props.read}</td>
    </tr>
  );
};

export default TableRow;
