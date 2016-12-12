import React from "react";
import Button from 'react-bootstrap/lib/Navbar';

const navBarInstance = (
	<Navbar>
		<Navbar.Header>
      		<Navbar.Brand>
        		<a href="#">Brand</a>
      		</Navbar.Brand>
      		<Navbar.Toggle />
    	</Navbar.Header>

    	<Navbar.Collapse>
      		<Navbar.Form pullLeft>
        		<FormGroup>
          			<FormControl type="text" placeholder="Search" />
        		</FormGroup>
        		{' '}
       			<Button type="submit">Search</Button>
      		</Navbar.Form>

    </Navbar.Collapse>



    	<Navbar.Text pullRight>
        	Signed in as: <Navbar.Link href="#">Mark Otto</Navbar.Link>
        </Navbar.Text>



  </Navbar>
);






