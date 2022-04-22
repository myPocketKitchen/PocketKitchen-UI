import dotenv from "dotenv";
dotenv.config(); // parse .env file and assign to process.env

export default {
  port: parseInt(process.env.PORT, 10),
  mongoURL: process.env.KEY,
  lakeURL: process.env.LAKE_KEY,
};