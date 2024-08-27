import AddProduct from "./addProduct";
import UpdateProduct from "./updateProduct";
import DeleteProduct from "./deleteProduct";

import { createContext, useEffect, useRef, useState } from "react";
import { useDisclosure } from "@chakra-ui/react";

export const usefetch = createContext();

function SearchProducts() {
  const [filter, setFilter] = useState("");
  const [searchKeyword, setSearchKeyword] = useState("");
  const [listproduct, setListProduct] = useState([]);
  const [skip, setSkip] = useState(0);
  const [limit, setLimit] = useState(10);
  const index = useRef(0);
  const { isOpen, onOpen, onClose } = useDisclosure();
  const ModalType = useRef("");
  const _id = useRef("");
  const cancelRef = useRef();
  const count = useRef(0);

  // Fetch Data from backend

  const fetchProducts = async (filterBy, searchInput) => {
    await fetch(
      `http://127.0.0.1:8000/product?filterBy=${filterBy}&SearchText=${searchInput}&limit=${limit}&skip=${skip}`
    )
      .then((res) => res.json())
      .then((data) => {
        setListProduct(data.products);
        count.current = data.count;
      });
  };

  // onload fill the table

  useEffect(() => {
    fetchProducts(filter, searchKeyword);
  }, [skip, limit]);

  return (
    <>
      <usefetch.Provider value={fetchProducts}>
        <div className="d-flex justify-content-around mb-3">
          {/* This is Filter */}

          <div className="p-2">
            <select
              onChange={(e) => setFilter(e.target.value)}
              className="form-select"
              aria-label="Default select example"
            >
              <option value="">Filter By :</option>
              <option value="name">Name</option>
              <option value="unit">Unit</option>
              <option value="price">Price</option>
              <option value="LowerPrice">LowerPrice</option>
              <option value="GreaterPrice">GreaterPrice</option>
            </select>
          </div>

          {/* This is Search Input */}

          <div className="p-2 input-group">
            <input
              onChange={(e) => setSearchKeyword(e.target.value)}
              type="text"
              className="form-control"
              placeholder="Search..."
            />
          </div>

          {/* This is Search Button */}

          <div className="p-2 d-flex justify-content-evenly">
            <button
              onClick={() => fetchProducts(filter, searchKeyword)}
              type="button"
              className="btn btn-outline-dark"
            >
              Search
            </button>
            &nbsp;
            <button
              onClick={() => {
                ModalType.current = "ADD";
                onOpen();
              }}
              type="button"
              className="btn btn-outline-success"
            >
              Add
            </button>
          </div>
        </div>

        {/* This is Add Product Modal */}

        {ModalType.current === "ADD" ? (
          <AddProduct isOpen={isOpen} onClose={onClose} />
        ) : ModalType.current === "EDIT" ? (
          <UpdateProduct ID={_id.current} isOpen={isOpen} onClose={onClose} />
        ) : (
          <DeleteProduct
            ID={_id.current}
            isOpen={isOpen}
            onClose={onClose}
            cancelRef={cancelRef}
          />
        )}

        {/* This is Limit */}

        <div className="d-flex justify-content-between">
          <div style={{ width: "100px" }}>
            <select
              onChange={(e) => {
                if (e.target.selectedIndex !== 0) {
                  setSkip(0);
                  setLimit(parseInt(e.target.value));
                }
              }}
              className="form-select form-select-sm"
            >
              <option value="">Rows</option>
              <option value="10">10</option>
              <option value="50">50</option>
              <option value="100">100</option>
            </select>
          </div>
          <nav aria-label="Page navigation example">
            <ul className="pagination">
              <li className="page-item">
                <button
                  onClick={() => {
                    setSkip(0);
                  }}
                  className="page-link"
                >
                  First
                </button>
              </li>
              <li className="page-item">
                <button
                  onClick={() => {
                    skip >= limit && setSkip(skip - limit);
                  }}
                  className="page-link"
                >
                  Prev
                </button>
              </li>
              <li className="page-item">
                <button
                  onClick={() => {
                    if (skip + limit < count.current) {
                      setSkip(skip + limit);
                    }
                  }}
                  className="page-link"
                >
                  Next
                </button>
              </li>
              <li
                onClick={() => {
                  setSkip(count.current - (count.current % limit));
                }}
                className="page-item"
              >
                <button className="page-link">Last</button>
              </li>
            </ul>
          </nav>
        </div>

        {/* This is Product List */}

        <div>
          <table className="table table-bordered">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Unit</th>
                <th scope="col">Price</th>
                <th scope="col" style={{ width: "150px", textAlign: "center" }}>
                  Action
                </th>
              </tr>
            </thead>
            <tbody>
              {listproduct.map((product, i) => (
                <tr key={product._id}>
                  <td>{(index.current = skip + i + 1)}</td>
                  <td>{product.name}</td>
                  <td>{product.unit}</td>
                  <td>{product.price}</td>
                  <td>
                    <button
                      onClick={() => {
                        ModalType.current = "EDIT";
                        _id.current = product._id;
                        onOpen();
                      }}
                      className="btn btn-outline-primary"
                    >
                      Edit
                    </button>
                    <button
                      onClick={() => {
                        ModalType.current = "DELETE";
                        _id.current = product._id;
                        onOpen();
                      }}
                      className="btn btn-outline-danger"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
              <tr>
                <td colSpan="4"></td>
              </tr>
            </tbody>
          </table>
        </div>
      </usefetch.Provider>
    </>
  );
}

export default SearchProducts;
