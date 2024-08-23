import { Select, Input, Button, Flex } from "@chakra-ui/react";
import ProductModal from "./ProductModal";

function Header(props) {
  const searchInput = props.searchInput;
  const searchMethod = props.searchMethod;

  return (
    <>
      <Flex spacing={3} marginY={10} marginX={5}>
        <Select
          placeholder="Filter By"
          id="filterDrop"
          width="150px"
          size="md"
          mr="1"
          onChange={(e) => {
            searchMethod(e);
          }}
        >
          <option value="name">Name</option>
          <option value="unit">Unit</option>
          <option value="price">Price</option>
          <option value="LowerPrice">Lower than price</option>
          <option value="GreaterPrice">Greater than price</option>
        </Select>
        <Input
          id="searchInput"
          onChange={(e) => {
            searchInput(e);
          }}
          placeholder="Search"
          size="md"
          mr="1"
        />
        <ProductModal class_name="success" id="" val="Add Product" />
      </Flex>
    </>
  );
}

export default Header;
