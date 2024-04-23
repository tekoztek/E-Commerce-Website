import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

function SearchBox() {
    const [keyword, setKeyword] = useState('');
    let navigate = useNavigate();  // Use 'navigate' to reflect the function it provides

    const submitHandler = (e) => {
        e.preventDefault();
        if (keyword.trim()) {
            navigate(`/?keyword=${keyword.trim()}&page=1`);
        } else {
            navigate('/');  // Navigate to the home page or retain the current page
        }
    };

    return (
        <Form onSubmit={submitHandler} className="d-inline-flex">
            <Form.Control
                type="text"
                name="q"
                placeholder="Search"
                className="mr-sm-2"
                value={keyword}
                onChange={(e) => setKeyword(e.target.value)}
            />
            <Button type="submit" variant="outline-success" className="mb-2">
                Submit
            </Button>
        </Form>
    );
}

export default SearchBox;
