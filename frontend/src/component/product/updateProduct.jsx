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
import { useContext, useEffect, useState } from "react";
import { usefetch } from "./searchProducts";

function UpdateProduct({ isOpen, onClose, ID }) {
  const fetchProducts = useContext(usefetch);
  const [product, setProduct] = useState({
    name: "",
    unit: "",
    price: 0,
  });

  // fetch Product Information
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/product/${ID}`)
      .then((res) => res.json())
      .then((data) => setProduct(data.product));
  }, []);

  // PUT Method
  const handleUpdate = () => {
    fetch(`http://127.0.0.1:8000/product/${ID}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(product),
    }).then(fetchProducts("", ""));
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Update Product</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          <div className="form-floating mb-3">
            <input
              value={product.name}
              onChange={(e) => {
                setProduct((p) => ({ ...p, name: e.target.value }));
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
              value={product.unit}
              className="form-select"
              id="floatingSelectUnit"
              onChange={(e) => {
                setProduct((p) => ({ ...p, unit: e.target.value }));
              }}
            >
              <option value="kg">kg</option>
              <option value="each">each</option>
            </select>
            <label htmlFor="floatingSelectUnit">Unit</label>
          </div>
          <div className="form-floating  mb-3">
            <input
              value={product.price}
              onChange={(e) => {
                setProduct((p) => ({ ...p, price: e.target.value }));
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
            }}
          >
            Cancel
          </Button>
          <Button
            onClick={() => {
              handleUpdate();
              onClose();
            }}
            colorScheme="blue"
          >
            Edit
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
}

export default UpdateProduct;
