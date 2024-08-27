import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Button,
} from "@chakra-ui/react";
import { useContext, useState } from "react";
import { usefetch } from "./searchProducts";

function AddProduct({ isOpen, onClose }) {
  const fetchProducts = useContext(usefetch);
  const [product, setProduct] = useState({
    name: "",
    unit: "",
    price: 0,
  });

  const handleInsert = async () => {
    fetch("http://127.0.0.1:8000/product", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(product),
    }).then(fetchProducts("", ""));
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Insert Product</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          <div className="form-floating mb-3">
            <input
              onChange={(e) => {
                setProduct((p) => ({
                  ...p,
                  name: e.target.value,
                }));
              }}
              type="text"
              className="form-control"
              id="floatingInputName"
              placeholder=""
            />
            <label htmlFor="floatingInputName">Name</label>
          </div>
          <div className="form-floating  mb-3">
            <select
              onChange={(e) => {
                e.target.selectedIndex !== 0 &&
                  setProduct((p) => ({
                    ...p,
                    unit: e.target.value,
                  }));
              }}
              className="form-select"
              id="floatingSelectUnit"
            >
              <option>Select Unit</option>
              <option value="kg">kg</option>
              <option value="each">each</option>
            </select>
            <label htmlFor="floatingSelectUnit">Unit</label>
          </div>
          <div className="form-floating mb-3">
            <input
              onChange={(e) => {
                setProduct((p) => ({
                  ...p,
                  price: parseInt(e.target.value),
                }));
              }}
              type="text"
              className="form-control"
              id="floatingInputPrice"
              placeholder=""
            />
            <label htmlFor="floatingPassword">Price</label>
          </div>
        </ModalBody>

        <ModalFooter>
          <Button
            mr={3}
            onClick={() => {
              onClose();
              fetchProducts("", "");
            }}
          >
            Cancel
          </Button>
          <Button
            onClick={() => {
              handleInsert();
              onClose();
            }}
            colorScheme="green"
          >
            Insert
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
}

export default AddProduct;
