import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Button,
  AlertDialog,
  AlertDialogBody,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogContent,
  AlertDialogOverlay,
} from "@chakra-ui/react";
import { useContext, useState, useRef } from "react";
import { ProductContext } from "./Product";

function ProductModal(props) {
  const class_name = props.class_name;
  const val = props.val;
  const id = props.id;
  const [product, setProduct] = useState({
    Name: "",
    Unit: "",
    Price: 0,
  });
  const { isOpen, onOpen, onClose } = useDisclosure();
  const apiURL = `http://127.0.0.1:8000/product/${id}`;
  const { products, product_refresh } = useContext(ProductContext);
  const cancelRef = useRef();

  // Show Product / Get Method
  const ShowProduct = async () => {
    if (id)
      await fetch(apiURL)
        .then((response) => response.json())
        .then((data) => setProduct(data.product));
  };

  const clearInputs = () => {
    document.getElementById("filterDrop").selectedIndex = 0;
    document.getElementById("searchInput").value = "";
  };

  // Insert Product / Post Method

  const handleInsert = async () => {
    console.log(product);
    if (product.Name === "") console.log("Please Set Product Name");
    else if (product.Unit === "") console.log("Please Set Product Unit");
    else if (product.Price <= 0) console.log("Please Set Product Price");
    else {
      await fetch("http://127.0.0.1:8000/product", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: product.Name,
          unit: product.Unit,
          price: product.Price,
        }),
      })
        .then(product_refresh)
        .then(clearInputs);
      onClose();
    }
  };

  // Update Product / Put Method
  const handleUpdate = async () => {
    await fetch(apiURL, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: product.Name,
        unit: product.Unit,
        price: product.Price,
      }),
    })
      .then(product_refresh)
      .then(clearInputs);
    onClose();
  };

  // Delete Product / Delete Method
  const handleDelete = async () => {
    await fetch(apiURL, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: { _id: product._id },
    })
      .then(product_refresh)
      .then(clearInputs);
    onClose();
  };

  return (
    <>
      <input
        type="button"
        className={"btn btn-outline-" + class_name}
        value={val}
        onClick={() => {
          onOpen();
          ShowProduct();
        }}
      />
      {val == "Edit" ? (
        <Modal isOpen={isOpen} onClose={onClose}>
          <ModalOverlay />
          <ModalContent>
            <ModalHeader>Update Product</ModalHeader>
            <ModalCloseButton />
            <ModalBody>
              <div className="form-floating mb-3">
                <input
                  value={product.Name}
                  onChange={(e) => {
                    setProduct((p) => ({ ...p, Name: e.target.value }));
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
                  value={product.Unit}
                  className="form-select"
                  id="floatingSelectUnit"
                  onChange={(e) => {
                    setProduct((p) => ({ ...p, Unit: e.target.value }));
                  }}
                >
                  <option value="kg">kg</option>
                  <option value="each">each</option>
                </select>
                <label htmlFor="floatingSelectUnit">Unit</label>
              </div>
              <div className="form-floating  mb-3">
                <input
                  value={product.Price}
                  onChange={(e) => {
                    setProduct((p) => ({ ...p, Price: e.target.value }));
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
              <Button mr={3} onClick={onClose}>
                Cancel
              </Button>
              <Button onClick={handleUpdate} colorScheme="blue">
                Edit
              </Button>
            </ModalFooter>
          </ModalContent>
        </Modal>
      ) : val == "Delete" ? (
        <AlertDialog
          isOpen={isOpen}
          leastDestructiveRef={cancelRef}
          onClose={onClose}
        >
          <AlertDialogOverlay>
            <AlertDialogContent>
              <AlertDialogHeader fontSize="lg" fontWeight="bold">
                Delete Product
              </AlertDialogHeader>

              <AlertDialogBody>
                Are you sure? You can't undo this action afterwards.
              </AlertDialogBody>

              <AlertDialogFooter>
                <Button ref={cancelRef} onClick={onClose}>
                  Cancel
                </Button>
                <Button colorScheme="red" onClick={handleDelete} ml={3}>
                  Delete
                </Button>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialogOverlay>
        </AlertDialog>
      ) : (
        <Modal isOpen={isOpen} onClose={onClose}>
          <ModalOverlay />
          <ModalContent>
            <ModalHeader>Insert Product</ModalHeader>
            <ModalCloseButton />
            <ModalBody>
              <div className="form-floating mb-3">
                <input
                  onChange={(e) => {
                    setProduct((p) => ({ ...p, Name: e.target.value }));
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
                  className="form-select"
                  id="floatingSelectUnit"
                  onChange={(e) => {
                    setProduct((p) => ({ ...p, Unit: e.target.value }));
                  }}
                >
                  <option>Select Unit</option>
                  <option value="kg">kg</option>
                  <option value="each">each</option>
                </select>
                <label htmlFor="floatingSelectUnit">Unit</label>
              </div>
              <div className="form-floating  mb-3">
                <input
                  onChange={(e) => {
                    setProduct((p) => ({ ...p, Price: e.target.value }));
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
              <Button mr={3} onClick={onClose}>
                Cancel
              </Button>
              <Button onClick={handleInsert} colorScheme="green">
                Insert
              </Button>
            </ModalFooter>
          </ModalContent>
        </Modal>
      )}
    </>
  );
}

export default ProductModal;
