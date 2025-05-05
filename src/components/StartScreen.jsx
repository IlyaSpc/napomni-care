// src/components/StartScreen.jsx
import { Box, Button, Typography } from "@mui/material";
import { useEffect, useState } from "react";

export default function StartScreen({ onStart }) {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    setTimeout(() => setVisible(true), 2000); // анимация через 2 сек
  }, []);

  return (
    <Box
      display="flex"
      height="100vh"
      alignItems="center"
      justifyContent="center"
      flexDirection="column"
      bgcolor="#6633cc"
      color="white"
    >
      <Typography variant="h4" gutterBottom>Напомни мне</Typography>
      {visible && (
        <Button
          variant="contained"
          onClick={onStart}
          sx={{ mt: 2, bgcolor: "white", color: "#6633cc" }}
        >
          начать
        </Button>
      )}
    </Box>
  );
}
