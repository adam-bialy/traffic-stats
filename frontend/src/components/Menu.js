const Menu = (props) => {
  const handleChange = (event) => {
    props.changeGroup(event.target.value);
  };

  return (
    <>
      <h3>Select filter to group visits by:</h3>
      <select name="group" onChange={handleChange} value={props.group}>
        <option value="location">Location</option>
        <option value="date">Date</option>
      </select>
    </>
  );
};

export default Menu;
