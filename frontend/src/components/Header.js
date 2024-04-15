import React from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Row from 'react-bootstrap/Row';
import {LinkContainer} from 'react-router-bootstrap'

const Header = () => {
  return (
    <header>
      <Navbar expand="lg" bg="dark" variant="dark" collapseOnSelect>
        <Container>
			<LinkContainer to='/'>
				<Navbar.Brand>ProShop</Navbar.Brand>
			</LinkContainer>
					<Navbar.Toggle aria-controls="basic-navbar-nav" />
					<Navbar.Collapse id="basic-navbar-nav">
						<Nav className="mr-auto">
							<LinkContainer to='/cart'>
								<Nav.Link><i className="fas fa-shopping-cart px-2"></i>Cart</Nav.Link>
							</LinkContainer>
							<LinkContainer to='/login'>
								<Nav.Link><i className="fas fa-user px-2"></i>Login</Nav.Link>
							</LinkContainer>
						</Nav>
					</Navbar.Collapse>
        </Container>
    	</Navbar>
    </header>
  )
}

export default Header

