import TableRow from "./TableRow";
import classes from "./Table.module.css";

const Table = (props) => {
  const totalOpen = props.data.reduce((sum, current) => sum + current.open, 0);
  const totalView = props.data.reduce((sum, current) => sum + current.view, 0);
  const totalRead = props.data.reduce((sum, current) => sum + current.read, 0);

  return (
    <table className={classes.table}>
      <thead>
        <tr>
          <th>{props.group.replace("_", " ")}</th>
          <th>Opened</th>
          <th>Viewed</th>
          <th>Read</th>
        </tr>
      </thead>
      <tbody>
        {props.data.map((row, index) => (
          <TableRow group={props.group} {...row} key={index} />
        ))}
        <tr>
          <th>Total</th>
          <th>{totalOpen}</th>
          <th>{totalView}</th>
          <th>{totalRead}</th>
        </tr>
      </tbody>
    </table>
  );
};

export default Table;
