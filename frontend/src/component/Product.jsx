import { createContext, useEffect, useRef, useState } from "react";
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
  const [skip, setSkip] = useState(0);
  const [limit, setLimit] = useState(10);
  const [valueInput, setValueInput] = useState("");
  const AlertMessage = useRef("");

  // for alert
  const {
    isOpen: isVisible,
    onClose,
    onOpen,
  } = useDisclosure({ defaultIsOpen: false });

  // Fetch Products / Get Method => this is ajoutable you need to remove it when fix all
  const product_refresh = async () => {
    const apiURL = "http://127.0.0.1:8000/product";
    await fetch(apiURL)
      .then((response) => response.json())
      .then((data) => setProducts(data.products));
  };

  const handleFilterBy = (e) => {
    setFilterBy(e.target.value);
    product_refresh();
  };

  const fetchDataBy = async (filterBy, searchInput) => {
    const url = `http://127.0.0.1:8000/product?filterBy=${filterBy}&SearchText=${searchInput}&skip=${skip}`;
    await fetch(url)
      .then((res) => res.json())
      .then((data) => setProducts(data.products));
  };

  const handleSearch = async (e) => {
    const searchInput = e.target.value;
    setSkip(0);
    setValueInput(e.target.value);

    if (!searchInput) {
      onClose();
      product_refresh();
    } else {
      if (filterBy === "") {
        AlertMessage.current = "Must select filter by to search";
        onOpen();
      } else if (
        filterBy === "price" ||
        filterBy === "LowerPrice" ||
        filterBy === "GreaterPrice"
      ) {
        if (searchInput % 1 !== 0) {
          AlertMessage.current = "Search must be a Number";
          onOpen();
        } else {
          fetchDataBy(filterBy, searchInput);
        }
      } else {
        fetchDataBy(filterBy, searchInput);
      }
    }
  };

  useEffect(() => {
    fetchDataBy(filterBy, searchInput);
  }, []);
  useEffect(() => {
    fetchDataBy(filterBy, valueInput);
  }, [skip, limit]);

  return (
    <ProductContext.Provider value={{ products, product_refresh }}>
      <>
        {isVisible && (
          <Alert status="error">
            <AlertIcon />
            <Flex>
              <Box>
                <AlertTitle>Error!</AlertTitle>
                <AlertDescription>{AlertMessage.current}!</AlertDescription>
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
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td>
                <nav aria-label="Page navigation example">
                  <ul className="pagination">
                    <li className="page-item">
                      <button
                        onClick={() => {
                          if (skip >= limit) {
                            setSkip(skip - limit);
                          }
                        }}
                        className="page-link"
                      >
                        Previous
                      </button>
                    </li>
                    <li className="page-item">
                      <button className="page-link">1</button>
                    </li>
                    <li className="page-item">
                      <button className="page-link">2</button>
                    </li>
                    <li className="page-item">
                      <button className="page-link">3</button>
                    </li>
                    <li className="page-item">
                      <button
                        onClick={() => {
                          setSkip(skip + limit);
                        }}
                        className="page-link"
                      >
                        Next
                      </button>
                    </li>
                  </ul>
                </nav>
              </td>
            </tr>
          </tbody>
        </table>
        <ProductModal />
      </>
    </ProductContext.Provider>
  );
}

export default Product;
