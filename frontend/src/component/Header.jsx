import { Select, Input, Button, Flex } from "@chakra-ui/react";
import ProductModal from "./ProductModal";
import { createContext } from "react";

export const useValueInput = createContext();

function Header(props) {
  const searchInput = props.searchInput;
  const searchMethod = props.searchMethod;

  return (
    <>
      <Flex spacing={3} marginY={10} marginX={5}>
        <select
          className="form-select"
          id="filterDrop"
          style={{
            width: "150px",
            marginRight: 1,
          }}
          onChange={(e) => {
            searchMethod(e);
            document.getElementById("searchInput").value = "";
          }}
        >
          <option value="">Filter By</option>
          <option value="name">Name</option>
          <option value="unit">Unit</option>
          <option value="price">Price</option>
          <option value="LowerPrice">Lower than price</option>
          <option value="GreaterPrice">Greater than price</option>
        </select>
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
