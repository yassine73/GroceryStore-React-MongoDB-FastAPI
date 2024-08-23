import { createContext, useContext, useEffect, useRef, useState } from "react";
import ProductModal from "./ProductModal";
import Header from "./Header";
import {
  Alert,
  AlertIcon,
  useDisclosure,
  CloseButton,
  Box,
  AlertTitle,
  AlertDescription,
  Flex,
} from "@chakra-ui/react";

export const ProductContext = createContext();

function Product() {
  const [products, setProducts] = useState([]);
  const [filterBy, setFilterBy] = useState("");

  // for alert
  const {
    isOpen: isVisible,
    onClose,
    onOpen,
  } = useDisclosure({ defaultIsOpen: false });

  // Fetch Products / Get Method
  const product_refresh = async () => {
    const apiURL = "http://127.0.0.1:8000/product";
    await fetch(apiURL)
      .then((response) => response.json())
      .then((data) => setProducts(data.products));
  };

  const handleFilterBy = (e) => {
    setFilterBy(e.target.value);
  };

  const handleSearch = async (e) => {
    const searchInput = e.target.value;
    if (searchInput) {
      if (filterBy) {
        const url = `http://127.0.0.1:8000/product/?filterBy=${filterBy}&SearchText=${searchInput}`;
        fetch(url)
          .then((res) => res.json())
          .then((data) => setProducts(data.products));
      } else {
        console.log("Must select filter by to search");
        onOpen();
      }
    } else product_refresh();
  };

  useEffect(() => {
    product_refresh();
  }, []);

  return (
    <ProductContext.Provider value={{ products, product_refresh }}>
      <>
        {isVisible && (
          <Alert status="error">
            <AlertIcon />
            <Flex>
              <Box>
                <AlertTitle>Error!</AlertTitle>
                <AlertDescription>
                  Please Select which Filter you want to search with!
                </AlertDescription>
              </Box>
              <CloseButton
                alignSelf="flex-start"
                position="relative"
                right={-1}
                top={-1}
                onClick={onClose}
              />
            </Flex>
          </Alert>
        )}
        <Header
          searchInput={(e) => handleSearch(e)}
          searchMethod={(e) => handleFilterBy(e)}
        />
        <table className="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Name</th>
              <th scope="col">Unit</th>
              <th scope="col">Price</th>
              <th style={{ width: "100px", textAlign: "center" }} scope="col">
                Action
              </th>
            </tr>
          </thead>
          <tbody>
            {products.map((product, index) => (
              <tr key={product._id}>
                <td>{index + 1}</td>
                <td>{product.Name}</td>
                <td>{product.Unit}</td>
                <td>{product.Price}</td>
                <td align="right">
                  <div className="btn-group">
                    <ProductModal
                      class_name="primary"
                      id={product._id}
                      val="Edit"
                    />
                    <ProductModal
                      class_name="danger"
                      id={product._id}
                      val="Delete"
                    />
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <ProductModal />
      </>
    </ProductContext.Provider>
  );
}

export default Product;
